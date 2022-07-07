// x and y position of the bob
float ux = 400; // 300 
float uy = 50; // 100
float px = 0;
float py = 0;

// x and y position of the anchor point
float tx = 0;
float ty = 0;

float k = 0.1; // spring constant
float m = 20; // mass
float b = 0; // damping constant
float g = 1; // acceleration due to gravity

float r = uy; // length at equilibrium
float l = 0; // length of the spring
float s = 0; // displacement from rest length when spring is stretched

float acc_x = 0;
float vel_x = 0;
float acc_y = 0;
float vel_y = 0;

PGraphics buffer;

void setup() {
  size(800,700);
  strokeWeight(4);
  buffer = createGraphics(width,height);
}

void draw() {
  background(220);
  translate(width/2,30);
  image(buffer, -400, 0, width, height);
  
  l = sqrt((ux-tx)*(ux-tx)+(uy-ty)*(uy-ty));
  s = l-r;
  
  acc_x = -k/m*s*((ux-tx)/l)-b/m*vel_x;
  acc_y = g-k/m*s*((uy-ty)/l)-b/m*vel_y;
  
  vel_x += acc_x;
  vel_y += acc_y;
  
  ux += vel_x;
  uy += vel_y;
  
  if (frameCount>1) {
    buffer.beginDraw();
    buffer.strokeWeight(2);
    buffer.line(ux+400,uy,px+400,py);
    buffer.endDraw();
  }
  
  line(0,0,ux,uy);
  circle(ux,uy,40);
  
  px = ux;
  py = uy;
}
