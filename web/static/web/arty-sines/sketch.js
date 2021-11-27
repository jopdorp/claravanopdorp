
function setup() {
  createCanvas(400, 300, WEBGL);
  noStroke();
}

function draw() {
  translate(
        0,
        0,
        -300
      );
  background(255);

  ambientLight(50);
  specularColor(10, 0, 0);
  pointLight(20, 20, 20, 20, -50, 50);
  specularColor(0, 10, 0);
  pointLight(200, 200, 200, 100, 50, 50);
  specularMaterial(255);


  rotateY(- mouseX / 500 + 9.7);
  rotateX(- mouseY / 500 + 9.8);

  for (let j = 0; j < 20; j++) {
    push();
    for (let i = 0; i < 4; i++) {
      translate(
        sin(frameCount * 0.003 + j) * 150,
        sin(frameCount * 0.001 + j) * 100,
        cos(0.04 + i+j) * 80
      );
      rotateZ(frameCount * 0.00001 + 20);
      push();
      sphere(
        1.2 + cos((frameCount + 200) * 0.001 *  (i+j)) * 3,
        4,
        4
      );
      pop();
    }
    pop();
  }
}

