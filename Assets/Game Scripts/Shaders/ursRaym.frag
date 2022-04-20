#version 140

uniform sampler2D p3d_Texture0;
uniform vec4 p3d_ColorScale;
in vec2 texcoord;
in vec3 world_normal;
out vec4 fragColor;


void main() {
    vec4 norm = vec4(world_normal*0.5+0.5, 1);
    float grey = 0.21 * norm.r + 0.71 * norm.g + 0.07 * norm.b;
    norm = vec4(grey, grey, grey, 1);
    vec4 color = texture(p3d_Texture0, texcoord) * p3d_ColorScale * norm;
    fragColor = color.rgba;
}