int Trigger = 6;
int Echo    = 7;
int LED     = 2;

int distancia = 0;
int tempo     = 0;

void setup()
{
    pinMode(Trigger, OUTPUT);
    pinMode(Echo,    INTPUT);
    pinMode(LED,     OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    digitalWrite(Trigger, LOW); //Estabilizamos o sensor
    delayMicroseconds(2);
    digitalWrite(Trigger, HIGH); //Se envia o pulso ultrassônico
    delayMicroseconds(10);
    /* Mede o tempo transcorrido entre o envio e recebimento */
    tempo = pulseIn(Echo, HIGH);

    // converte para distância
    distancia = int(tempo * 0.017); // em cm

    if (distancia < 10) 
    {
        digitalWrite(LED, HIGH);
    }
    else
    {
        digitalWrite(LED, LOW);
    }
    
}
