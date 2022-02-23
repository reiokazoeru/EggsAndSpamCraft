const int MAX_MARCHING_STEPS = 255;
const float MIN_DIST = 0.0;
const float MAX_DIST = 100.0;
const float PRECISION = 0.001;

struct Surface {
  float signedDistance;
  vec3 color;
};
vec4 sdCube(vec3 p, float r, vec3 offset, vec3 col )
{
  float d1 = max(length(p.x-offset.x)-r,length(p.y-offset.y)-r);
  float d = max(d1,length(p.z-offset.z)-r);
  return vec4(d, col);
}

vec4 sdSphere(vec3 p, float r, vec3 offset, vec3 col )
{
  float d = length(p - offset) - r;
  return vec4(d, col);
}

vec4 sdFloor(vec3 p, vec3 col) {
  float d = p.y + 1.;
  return vec4(d, col);
}

vec4 minWithColor(vec4 obj1, vec4 obj2) {
  if (obj2.x < obj1.x) return obj2; // The x component of the object holds the "signed distance" value
  return obj1;
}

vec4 sdScene(vec3 p) {
  vec4 sphereLeft = sdCube(p, 0.25, vec3(-2.5,0, -2), vec3(0, .8, .8));
  vec4 sphereRight = sdSphere(p, 1., vec3(2.5, 0, -2), vec3(1, 0.58, 0.29));
  vec4 co = minWithColor(sphereLeft, sphereRight); // co = closest object containing "signed distance" and color
  co = minWithColor(co, sdFloor(p, vec3(0, 1, 0)));
  return co;
}

vec4 rayMarch(vec3 ro, vec3 rd, float start, float end) {
  float depth = start;
  vec4 co; // closest object

  for (int i = 0; i < MAX_MARCHING_STEPS; i++) {
    vec3 p = ro + depth * rd;
    co = sdScene(p);
    depth += co.x;
    if (co.x < PRECISION || depth > end) break;
  }
  
  vec3 col = vec3(co.yzw);

  return vec4(depth, col);
}

vec3 calcNormal(in vec3 p) {
    vec2 e = vec2(1.0, -1.0) * 0.0005; // epsilon
    return normalize(
      e.xyy * sdScene(p + e.xyy).x +
      e.yyx * sdScene(p + e.yyx).x +
      e.yxy * sdScene(p + e.yxy).x +
      e.xxx * sdScene(p + e.xxx).x);
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
  vec2 uv = (fragCoord-.5*iResolution.xy)/iResolution.y;
  vec3 backgroundColor = vec3(0.835, 1, 1);

  vec3 col = vec3(0);
  vec3 ro = vec3(0, 0, 3); // ray origin that represents camera position
  vec3 rd = normalize(vec3(uv, -1)); // ray direction

  vec4 co = rayMarch(ro, rd, MIN_DIST, MAX_DIST); // closest object

  if (co.x > MAX_DIST) {
    col = backgroundColor; // ray didn't hit anything
  } else {
    vec3 p = ro + rd * co.x; // point on sphere or floor we discovered from ray marching
    vec3 normal = calcNormal(p);
    vec3 lightPosition = vec3(2, 2, 7);
    vec3 lightDirection = normalize(lightPosition - p);

    // Calculate diffuse reflection by taking the dot product of 
    // the normal and the light direction.
    float dif = clamp(dot(normal, lightDirection), 0.3, 1.);

    // Multiply the diffuse reflection value by an orange color and add a bit
    // of the background color to the sphere to blend it more with the background.
    col = dif * co.yzw + backgroundColor * .2;
  }

  // Output to screen
  fragColor = vec4(col, 1.0);
}