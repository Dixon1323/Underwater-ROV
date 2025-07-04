#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

#define BLYNK_TEMPLATE_ID "TMPL31CsSoVKm"
#define BLYNK_TEMPLATE_NAME "Underwater"
#define BLYNK_AUTH_TOKEN "YxSb_mII2g7Qs65tWoHrbX4TrFC7_WJm"

char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "EDUREKA";
char pass[] = "Edureka@123456";
int data =0;
int status=0;


BLYNK_WRITE(V0) {
  data = param.asInt();
  if (data == 1) {
    forward();
  } else {
    stop();
  }
}

BLYNK_WRITE(V1) {
  data = param.asInt();
  if (data == 1) {
    reverse();
  } else {
    stop();
  }
}

BLYNK_WRITE(V2) {
  data = param.asInt();
  if (data == 1) {
    left();
  } else {
    stop();
  }
}

BLYNK_WRITE(V3) {
  data = param.asInt();
  if (data == 1) {
    right();
  } else {
    stop();
  }
}

void setup() {

  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);
  digitalWrite(D1, LOW);
  digitalWrite(D2, LOW);
  digitalWrite(D3, LOW);
  digitalWrite(D4, LOW);
  Serial.begin(9600);
  Serial.println("Connecting to WiFi");
  Blynk.begin(auth, ssid, pass, "blynk.cloud", 80);
  delay(6000);
}

void loop() {
  
    Blynk.run();
}


void reverse() {
  digitalWrite(D1, HIGH);
  digitalWrite(D2, LOW);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, LOW);
}

void forward() {
  digitalWrite(D1, LOW);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, LOW);
  digitalWrite(D4, HIGH);
}

void left() {
  digitalWrite(D1, HIGH);
  digitalWrite(D2, LOW);
  digitalWrite(D3, LOW);
  digitalWrite(D4, HIGH);
}

void right() {
  digitalWrite(D1, LOW);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, LOW);
}

void stop() {
  digitalWrite(D1, LOW);
  digitalWrite(D2, LOW);
  digitalWrite(D3, LOW);
  digitalWrite(D4, LOW);
}