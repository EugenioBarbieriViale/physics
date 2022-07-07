float r1 = 125;
float r2 = 125;

float m1 = 10;
float m2 = 10;

float a1 = PI/2;
float a2 = 0;

float a1_v = 0;
float a2_v = 0;

float x1 = 0;
float y1 = 0;
float x2 = 0;
float y2 = 0;
float px2 = 0;
float py2 = 0;

float g = 1;
PGraphics buffer;

void setup() {
  size(500, 500);
  strokeWeight(4);
  buffer = createGraphics(width, height);
}

void draw() {
  background(220);
  stroke(0);
  image(buffer, 0, 0, width, height);
  
  float num1 = -g * (2 * m1 + m2) * sin(a1);
  float num2 = -m2 * g * sin(a1 - 2 * a2);
  float num3 = -2 * sin(a1 - a2) * m2;
  float num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * cos(a1 - a2);
  float den = r1 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2));
  float a1_a = (num1 + num2 + num3 * num4) / den;

  num1 = 2 * sin(a1 - a2);
  num2 = (a1_v * a1_v * r1 * (m1 + m2));
  num3 = g * (m1 + m2) * cos(a1);
  num4 = a2_v * a2_v * r2 * m2 * cos(a1 - a2);
  den = r2 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2));
  float a2_a = (num1 * (num2 + num3 + num4)) / den;
  
  a1_v += a1_a;
  a2_v += a2_a;
  
  a1 += a1_v;
  a2 += a2_v;
  
  x1 = r1*sin(a1)+250;
  y1 = r1*cos(a1)+20;
  x2 = r2*sin(a2)+x1;
  y2 = r2*cos(a2)+y1;
  
  line(250,20,x1,y1);
  line(x1,y1,x2,y2);
  circle(x1,y1,20);
  circle(x2,y2,20);
  if (frameCount>1) {
    buffer.beginDraw();
    buffer.strokeWeight(2);
    buffer.line(x2,y2,px2,py2);
    buffer.endDraw();
  }
  
  px2 = x2;
  py2 = y2;
}
