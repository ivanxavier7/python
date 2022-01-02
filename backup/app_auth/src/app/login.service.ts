import { Injectable } from '@angular/core';
import {Observable, Subject} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor() { }
  private subject = new Subject<any>();

  sendClickEvent() {
    this.subject.next(new Subject());

  }

  getClickEvent():Observable<any>{
    return this.subject.asObservable();
  }
}
