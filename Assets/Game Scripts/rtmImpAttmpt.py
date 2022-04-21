from ursina import *



def dicToEnts(dic:dict):
    # take a list and create world entities (allows procedural entity creation)
    # format:
    # (((x1,y1,z1),(w1,l1,h1),(r1,p1,y1),(r1,g1,b1)),((x2,y2,z1),(w2,l2,h2),(r2,g2,b2)))
    entList =[]
    for rect in dic:
        print(rect)
        entList.append(Entity(
            model='cube',
            rotation=Vec3(rect[2][0],rect[2][1],rect[2][2]),
            color=rgb(rect[3][0],rect[3][1],rect[3][2]),
            position=rect[0],
            scale=rect[1]))
    return entList

def entsToShader(entL:list,cam):
    # take list of all entities and input their data into the shader
    shadL = []
    for i in entL:
        i.get_position()



def update(): #updates per frame
    camera.set_shader_input('iResolution',window.screen_resolution)
    entsToShader(cubez,camera)
    


cubes = [[[0,2,0],[1,1,5],[0,0,0],[255,255,255]]]


app = Ursina() # start runtime

# window setup
window.title = 'My Gex'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

#gex
shader = Shader(language=Shader.GLSL,
    vertex='''
    #version 430

    in vec4 p3d_Vertex;
    uniform mat4 p3d_ViewMatrixInverse;
    in vec2 p3d_MultiTexCoord0;
    out vec2 uv;

    void main() {
        gl_Position = p3d_ViewMatrixInverse  * p3d_Vertex;
        uv = p3d_MultiTexCoord0;
    }
    ''',

    fragment='''
    #version 430

    const int MAX_MARCHING_STEPS = 255;
    const float MIN_DIST = 0.0;
    const float MAX_DIST = 100.0;
    const float PRECISION = 0.001;
    
    uniform vec2 iResolution;
    in vec2 uv;
    out vec4 fragColor;


    struct Surface {
        float sd; // signed distance value
        vec3 col; // color
    };

    Surface sdSphere(vec3 p, float r, vec3 offset, vec3 col)
    {
        float d = length(p - offset) - r;
        return Surface(d, col);
    }

    Surface sdCube(vec3 p, float r, vec3 offset, vec3 col )
    {
        float d = max(max(length(p.x-offset.x)-r,length(p.y-offset.y)-r),length(p.z-offset.z)-r);
        return Surface(d, col);
    }
    
    Surface sdFloor(vec3 p, vec3 col) {
        float d = p.y + 1.;
        return Surface(d, col);
    }

    Surface minWithColor(Surface obj1, Surface obj2) {
        if (obj2.sd < obj1.sd) return obj2; // The sd component of the struct holds the "signed distance" value
        return obj1;
    }

    Surface sdScene(vec3 p) {
        //Surface sphereLeft = sdCube(p, 1., vec3(-2.5, 0, 2), vec3(0, .8, .8));
        Surface sphereRight = sdCube(p, 1., vec3(2.5, 2, -2), vec3(1, 0.58, 0.29));
        //Surface co = minWithColor(sphereLeft, sphereRight); // co = closest object containing "signed distance" and color
        //co = minWithColor(co, sdFloor(p, vec3(0, 1, 0)));
        return sphereRight;
    }

    Surface rayMarch(vec3 ro, vec3 rd, float start, float end) {
        float depth = start;
        Surface co; // closest object

        for (int i = 0; i < MAX_MARCHING_STEPS; i++) {
            vec3 p = ro + depth * rd;
            co = sdScene(p);
            depth += co.sd;
            if (co.sd < PRECISION || depth > end) break;
        }
        
        co.sd = depth;
        
        return co;
    }

    vec3 calcNormal(in vec3 p) {
        vec2 e = vec2(1.0, -1.0) * 0.0005; // epsilon
        return normalize(
        e.xyy * sdScene(p + e.xyy).sd +
        e.yyx * sdScene(p + e.yyx).sd +
        e.yxy * sdScene(p + e.yxy).sd +
        e.xxx * sdScene(p + e.xxx).sd);
    }

    void main()
    {
        vec3 backgroundColor = vec3(0.835, 1, 1);

        vec3 col = vec3(0);
        vec3 ro = vec3(0, 0, 3); // ray origin that represents camera position
        vec3 rd = normalize(vec3(uv, -1)); // ray direction

        Surface co = rayMarch(ro, rd, MIN_DIST, MAX_DIST); // closest object

        if (co.sd > MAX_DIST) {
            col = backgroundColor; // ray didn't hit anything
        } else {
            vec3 p = ro + rd * co.sd; // point on sphere or floor we discovered from ray marching
            vec3 normal = calcNormal(p);
            vec3 lightPosition = vec3(2, 2, 7);
            vec3 lightDirection = normalize(lightPosition - p);

            // Calculate diffuse reflection by taking the dot product of 
            // the normal and the light direction.
            float dif = clamp(dot(normal, lightDirection), 0.3, 1.);

            // Multiply the diffuse reflection value by an orange color and add a bit
            // of the background color to the sphere to blend it more with the background.
            col = dif * co.col + backgroundColor * .2;
        }

        // Output to screen
        fragColor = vec4(,1.0);
    }

    ''')
cube = Entity(model='cube',color=color.orange,scale=(2,2,2))

cubez = dicToEnts(cubes)
camera.shader = shader


app.run()