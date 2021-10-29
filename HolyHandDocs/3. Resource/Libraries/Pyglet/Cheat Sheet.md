### import pyglet
	imports the library (obviously)

### pyglet.window.Window()
	makes a window object

### pyglet.text.Label(\<content>,\<font_name>,\<font_size>,\<x>,\<y>,\<anchor_x>,\<anchor_y>)
	makes a text label

### pyglet.image.load(\<path>\)
	makes a image object (better ver of .resources.image) 
	Use with [[3. Resource/Libraries/os/Cheat Sheet]] to get root path and then path to 

### @window.event
	when window updates, run function below

### (window object).clear()
	clears the given window

### (label object).draw()
	draws label to window
	
### (image object).blit(\<x>,\<y>)
	draws image to window
	
### def on_draw() 
	function modifies draw function
	
### def on_key_press(symbol,modifiers)
	function that handles key presses

### def on_mosue_press(x,y,button,modifiers)
	function that handles mouse presses
### pyglet.resource.media(\<path>,streaming=\<bool>)
	load media as a var, for small sound effects set stream to false
	Use with [[3. Resource/Libraries/os/Cheat Sheet]] to get root path and 	then path to 