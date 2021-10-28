import pyglet -
	imports the library (obviously)

pyglet.window.Window() - 
	makes a window object

pyglet.text.Label(\<content>\,\<font_name>\,\<font_size>\,\<x>\,\<y>\,\<anchor_x>\,\<anchor_y>\)
	makes a text label

pyglet.resource.image(\<path>\)
	makes a image object

@window.event
	when window updates, run function below

(window object).clear()
	clears the given window

(label object).draw()
	draws label to window
	
(image object).blit(\<x>,\<y>)
	draws image to window