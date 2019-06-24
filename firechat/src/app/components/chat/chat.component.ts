import { Component, OnInit } from '@angular/core';
import {ChatService} from "../../providers/chat.service";


@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styles: []
})
export class ChatComponent implements OnInit {

  mensaje: string ="";	
  mensaje2: string ="";
  elemento: any; 
  elemento2: any; 

  constructor(public _cs: ChatService ) { 
    this._cs.cargarMensaje2().subscribe();

  	this._cs.cargarMensaje().subscribe( ()=>{

  		setTimeout( ()=>{
  			this.elemento.scrollTop = this.elemento.scrollHeight;
  			},20 )
  	}); 

  
    //this._cs.cargarMensaje2().subscribe();


  }



  ngOnInit(){
  	this.elemento=document.getElementById('app-mensajes');
  }

  enviar_mensaje(){
  	//console.log(this.mensaje);
  	if (this.mensaje.length===0){
  		return;
  	}

    Notification.requestPermission().then(()=> new Notification('Mensaje enviado correntamente'));

  	this._cs.agregarMensaje(this.mensaje)
  		.then( ()=>this.mensaje="" )
  		.catch( (err)=>console.error("Error al enviar",err ));

  }

  enviar_mensaje2(){
    console.log(this.mensaje);
    //this._cs.cargarMensaje2();
    if (this.mensaje.length===0){
      return;
    }

    this._cs.agregarMensaje2(this.mensaje)
      .then( ()=>this.mensaje="" )
      .catch( (err)=>console.error("Error al enviar",err ));

  }







}
