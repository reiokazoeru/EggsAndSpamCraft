vec3 getBackgroundColor(vec2 uv){
    uv += 0.5;
    vec3 gradientStartColor = vec3(1.,0.,1.);
    vec3 gradientEndColor = vec3(0.,1.,1.);
    return mix(gradientStartColor,gradientEndColor,uv.y);
}

float sdfCircle(vec2 uv, float r, vec2 offset){
    float x = uv.x - offset.x;
    float y = uv.y - offset.y;

    return length(vec2(x,y)) - r;
}

float sdfSquare(vec2 uv, float r, vec2 offset){
    float x = uv.x - offset.x;
    float y = uv.y - offset.y;

    return max(abs(x),abs(y)) - r;
}

vec3 drawScene(vec2 uv){
    vec3 col = getBackgroundColor(uv);
    float circle = sdfCircle(uv,0.1,vec2(0,0));
    float square = sdfSquare(uv, 0.07, vec2(0.1,0));

    col = mix(vec3(0.0, 0.0, 1.0), col, step(0., circle));
    col = mix(vec3(1.0, 0.0, 0.0), col, step(0.,square));

    return col;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord){
    vec2 uv = fragCoord/iResolution.xy;
    uv -= 0.5;
    uv.x *= iResolution.x/iResolution.y;

    vec3 col = drawScene(uv);

    fragColor = vec4(col,1.0);
}