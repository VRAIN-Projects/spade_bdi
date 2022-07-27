!start.

+!start : true
   <- ?slave1(X);
      .print("Enviando hacia", X);
      .send(slave1,achieve, saludar);
      .print("Fin del envio");
      .wait(100);
      .send(slave1,achieve,despedirse);
      .wait(100).