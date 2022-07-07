float x = 0;
float y = 0;
float k = 0.1;
float m = 20;
float b = 0.5;
float r = 290;

float vel = 0;
float acc = 0;

void setup() {
  size(600, 500);
  strokeWeight(3);
}

void draw() {
  background(220);
  translate(width/2,height/2);
  if (!mousePressed) {
    acc = (-k/m)*x-(b/m)*vel;
    vel += acc;
    x += vel;
  } else {
    x  = mouseX-width/2;
  }
  
  line(-r,0,x,y);
  circle(x,0,40);
}
