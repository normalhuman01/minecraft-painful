#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>

//the idea for the taser is use a small one that can work easily in 5-12V range.
//The schematic will by in a pdf on the github page. but the main idea is to control the current
//flow through a Mosfet

//port assignation
uint8_t MFControl = 13;

// Common Network with the MC SV
const char* ssid     = "";
const char* password = "";

//Create a webserver on any selected port
WebServer  server(3000  );

//Constants
const uint8_t SHOCKTIME = 500; //ms

void setup() {

  Serial.begin(115200);
  pinMode(MFControl, OUTPUT);

  
  digitalWrite(MFControl, LOW);

  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Waiting");
  }
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  

  // define conn routes
  server.on("/", handleOnConnect);
  server.on("/shock", shock);
  server.begin();
}

void loop() {
  server.handleClient();
}

void handleOnConnect(){
  server.send(200, "text/html", "<p>yuo ar ok</p>");
}

void shock(){
  Serial.println("Shocked");
  digitalWrite(MFControl, HIGH);
  delay(SHOCKTIME);
  digitalWrite(MFControl, LOW);
  server.send(200, "text/html", "");
}