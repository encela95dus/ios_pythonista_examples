# Template to run shadertoy examples
# current example contains code from shadertoy lesson1
#    https://www.shadertoy.com/view/Xd3Sz4
# You could try other lessons
# lesson 2 https://www.shadertoy.com/view/4scSz4
# lesson 5 https://www.shadertoy.com/view/4scSRN
# lesson 6 https://www.shadertoy.com/view/XdtSRN

import scene, ui



shadertoy_code  = '''
//include shadertoy here
//the following is the shadertoy code from https://www.shadertoy.com/view/Xd3Sz4
void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
	vec2 uv = fragCoord.xy / iResolution.xy;
    highp float pi = 3.14159265;

    // Uncomment one of the fragColor lines below to see what they do.
        
    // This makes the entire frame BLACK
	// fragColor = vec4(0, 0, 0, 0);

    // Gray gradient left-to-right.
    // fragColor = vec4(uv.x, uv.x, uv.x, 0);
    
    // Gray gradient bottom-to-top
    // fragColor = vec4(uv.y, uv.y, uv.y, 0);
    
    // Red gradient left-to-right + green gradient bottom-to-top.
    // fragColor = vec4(uv.x, uv.y, 0, 0);
    
    // red sin(16 * pi * x) gradient
    // green sin(9 * pi * y) gradeient
    fragColor = vec4(sin(uv.x* pi * 16.0),sin(uv.y * pi * 9.0),0,0);
    
    // Now, try to make diagonal bars!

}
'''

shader_text = '''
precision highp float;
varying vec2 v_tex_coord;
uniform sampler2D u_texture;
uniform float u_time;
uniform vec2 u_sprite_size;
uniform float u_scale;
uniform vec2 u_offset;

#define iGlobalTime u_time
#define iResolution (u_sprite_size*u_scale)
#define iMouse u_offset
#define iChannel0 u_texture

''' + shadertoy_code + '''
void main(void) {
    mainImage(gl_FragColor, gl_FragCoord.xy);
}
'''

class MyScene (scene.Scene):
    def setup(self):
        screen_size = ui.get_screen_size()
        self.sprite = scene.SpriteNode(
            size=screen_size,
            parent=self)
        self.sprite.shader = scene.Shader(shader_text)
        self.sprite.position = self.size/2
        
    def touch_began(self, touch):
        self.set_touch_position(touch)

    def touch_moved(self, touch):
        self.set_touch_position(touch)

    def set_touch_position(self, touch):
        dx, dy = self.sprite.position - touch.location
        self.sprite.shader.set_uniform('u_offset', (dx, dy))

scene.run(MyScene(), show_fps=True)
