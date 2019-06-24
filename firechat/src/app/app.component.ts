import { Component } from '@angular/core';

import { ChatService} from "./providers/chat.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(public _cs:ChatService) {
    //this.chats = db.collection('chats').valueChanges();
  }


  muestra( numerochat:string ){
    //console.log(numerochat);

    this._cs.mostrarestadochat(numerochat); 

  }
  


}
