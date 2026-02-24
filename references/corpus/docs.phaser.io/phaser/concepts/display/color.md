# Color | Phaser Help

Source: https://docs.phaser.io/phaser/concepts/display/color

On this page
Color
The Color class holds a single color value and allows for easy modification and reading of it.
Get color integer ​
Hex string, or color integer
var color = Phaser . Display . Color . ValueToColor ( input ) ;
input : Hex string, or color integer
RGB to color
var color = Phaser . Display . Color . GetColor ( red , green , blue ) ;
red , green , blue : 0 ~ 255
RGBA to color
var color = Phaser . Display . Color . GetColor32 ( red , green , blue , alpha ) ;
red , green , blue , alpha : 0 ~ 255
Hex string to color
var color = Phaser . Display . Color . HexStringToColor ( hex ) . color ;
hex : #0033ff , #03f , 0x0033ff , or 0x03f
RGB string to color
var color = Phaser . Display . Color . RGBStringToColor ( rgb ) ;
rgb : 'rgb(r,g,b)' , or 'rgba(r,g,b,a)'
r, g, b : 0 ~ 255
a : 0 ~ 1
HSV to color
var color = Phaser . Display . Color . HSVToRGB ( h , s , v ) . color ;
h , s , v : 0 ~ 1
Color integer to RGB ​
var rgb = Phaser . Display . Color . IntegerToRGB ( color ) ;
color : Color integer ( 0xAARRGGBB )
rgb : JSON object ( {r, g, b, a} )
HSV color wheel ​
Create color array
var colorArray = Phaser . Display . Color . HSVColorWheel ( s , v ) ;
Get color
var color = colorArray [ i ] . color ; // i : 0 ~ 359
Color object ​
Create color object ​
Create via r,g,b,a components
var color = new Phaser . Display . Color ( red , green , blue ) ; // alpha = 255
// var color = new Phaser.Display.Color(red, green, blue, alpha);
red , green , blue , alpha : 0 ~ 255
Create via color integer
var color = Phaser . Display . Color . IntegerToColor ( colorInteger ) ;
colorInteger : Color integer ( 0xAARRGGBB )
Set color ​
Set color
color . setTo ( red , green , blue ) ; // alpha = 255
// color.setTo(red, green, blue, alpha);
red , green , blue , alpha : 0 ~ 255
Set color in GL values
color . setGLTo ( red , green , blue ) ; // alpha = 1
// color.setTo(red, green, blue, alpha);
red , green , blue , alpha : 0 ~ 1
Set color from color object
color . setFromRGB ( rgba ) ;
rgba :
{
r : 0 ,
g : 0 ,
b : 0 ,
// a: 0
}
Set color from HSV
color . setFromHSV ( h , s , v ) ;
Set to transparent ()
color . transparent ( ) ;
Set (red, green, blue) to 0
Set to gray color
color . gray ( value ) ;
Set to a random color
color . random ( ) ;
or
color . random ( min , max ) ;
min : 0 ~ 255. Default value is 0.
max : 0 ~ 255. Default value is 255.
Set to random gray
color . randomGray ( ) ;
or
color . randomGray ( min , max ) ;
Set red/green/blue/alpha channel : 0 ~ 255
color . red = value ;
// color.red += value;
color . green = value ;
// color.green += value;
color . blue = value ;
// color.blue += value;
color . alpha = value ;
// color.alpha += value;
Set H/S/V channel : 0 ~ 1
color . h = value ;
// color.h += value;
color . s = value ;
// color.s += value;
color . v = value ;
// color.v += value;
Set normalized red, green, blue, alpha : 0 ~ 1
color . redGL = value ;
// color.redGL += value;
color . greenGL = value ;
// color.greenGL += value;
color . blueGL = value ;
// color.blueGL += value;
color . alphaGL = value ;
// color.alphaGL += value;
Set brighten
color . brighten ( value ) ;
value : Percentage, 0 ~ 100
Saturate : Increase the saturation (S) of this Color by the percentage amount given.
color . saturate ( value ) ;
value : Percentage, 0 ~ 100
Desaturate : Decrease the saturation (S) of this Color by the percentage amount given.
color . desaturate ( value ) ;
value : Percentage, 0 ~ 100
Lighten : Increase the lightness (V) of this Color by the percentage amount given.
color . lighten ( value ) ;
value : Percentage, 0 ~ 100
Darken : Decrease the lightness (V) of this Color by the percentage amount given.
color . darken ( value ) ;
value : Percentage, 0 ~ 100
Properties ​
RGB Color, not including the alpha channel
var c = color . color ;
RGB Color, including the alpha channel.
var c = color . color32 ;
RGB color string which can be used in CSS color values.
var c = color . rgba ;
Red, green, blue, alpha : 0 ~ 255
var r = color . red ;
var g = color . green ;
var b = color . blue ;
var a = color . alpha ;
H, S, V : 0 ~ 1
var h = color . h ;
var s = color . s ;
var v = color . v ;
Normalized red, green, blue, alpha : 0 ~ 1
var r = color . redGL ;
var g = color . greenGL ;
var b = color . blueGL ;
var a = color . alphaGL ;
Clone ​
var newColor = color . clone ( ) ;
To hex string ​
var hexString = Phaser . Display . Color . RGBToString ( color . r , color . g , color . b , color . a ) ;
// var hexString = Phaser.Display.Color.RGBToString(color.r, color.g, color.b, color.a, prefix);
Interpolation ​
Interpolate between 2 colors.
var colorOut = Phaser . Display . Color . Interpolate . RGBWithRGB ( r1 , g1 , b1 , r2 , g2 , b2 , length , index ) ;
var colorOut = Phaser . Display . Color . Interpolate . ColorWithColor ( color1 , color2 , length , index ) ;
var colorOut = Phaser . Display . Color . Interpolate . ColorWithRGB ( color , r , g , b , length , index ) ;
length , index : t = index/length (0~1)
Author Credits ​
Content on this page includes work by:
RexRainbow
Get color integer
Color integer to RGB
HSV color wheel
Color object
Create color object
Set color
Properties
Clone
To hex string
Interpolation
Author Credits
