import { Injectable } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/firestore';


import { Mensaje } from "../interface/mensaje.interface";
import { map } from "rxjs/operators"; 


import { AngularFireAuth } from '@angular/fire/auth';
import { auth } from 'firebase/app';


@Injectable({
  providedIn: 'root'
})
export class ChatService {
  private itemsCollection: AngularFirestoreCollection<Mensaje>;
  private itemsCollection2: AngularFirestoreCollection<Mensaje>;
 

  public chats: Mensaje[]=[];  
  public chats2: Mensaje[]=[]; 
  public usuario: any={};
  public contact: Array<Object>;
  public estadochat1: any="chat1";

  constructor(private afs: AngularFirestore, public afAuth: AngularFireAuth  ) {

      this.afAuth.authState.subscribe(user => {
      console.log('Estado del usuario ', user );

      if (!user){
        return;
      }
      this.usuario.nombre=user.displayName;
      this.usuario.uid=user.uid;
      this.contact = [];
      //console.log(user.displayName);
      //user.displayName.forEach( ( x ) => {

        //  this.contact.push( x );
      //} );





      })

   }

   mostrarestadochat(numerodechat:string ){
    this.estadochat1=numerodechat;
    console.log(this.estadochat1);
    return this.estadochat1;
   }





  login( proveedor:string  ) {


    if(proveedor==='google'){

      this.afAuth.auth.signInWithPopup(new auth.GoogleAuthProvider());
    }else{
      this.afAuth.auth.signInWithPopup(new auth.TwitterAuthProvider());
    }

  }
  logout() {
    this.usuario={};
    this.afAuth.auth.signOut();
  }





  cargarMensaje(){
  	this.itemsCollection = this.afs.collection<Mensaje>('chats', ref=>ref.orderBy('fecha','desc').limit(5));
  	return this.itemsCollection.valueChanges().pipe(map( (mensajes:Mensaje[])=>{
  											console.log(mensajes);

  											this.chats=[];
  											for (let mensaje of mensajes){
  												this.chats.unshift(mensaje);
  											}

  											return this.chats;}))
  											//this.chats=mensajes}))

  }

  cargarMensaje2(){

    this.itemsCollection2 = this.afs.collection<Mensaje>('chats2', ref=>ref.orderBy('fecha','desc').limit(5));
    return this.itemsCollection2.valueChanges().pipe(map( (mensajes:Mensaje[])=>{
                        console.log(mensajes);

                        this.chats2=[];
                        for (let mensaje of mensajes){
                          this.chats2.unshift(mensaje);
                        }

                        return this.chats2;}))
                        //this.chats=mensajes}))


  }




  agregarMensaje(texto : string ){
  	let mensaje: Mensaje={
  		nombre: this.usuario.nombre,
  		mensaje: texto,
  		fecha: new Date().getTime(),
      uid: this.usuario.uid

  	}
  	return this.itemsCollection.add(mensaje);

  }


  agregarMensaje2(texto : string ){
    
    console.log(this.usuario.nombre);
    let mensaje: Mensaje={

      nombre: this.usuario.nombre,
      mensaje: texto,
      fecha: new Date().getTime(),
      uid: this.usuario.uid

    }
    return this.itemsCollection2.add(mensaje);

  }


}
