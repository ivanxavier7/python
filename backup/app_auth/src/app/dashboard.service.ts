import { Injectable } from '@angular/core';
import {Contact} from "./contact.model";
import {environment} from "../environments/environment";
import {HttpClient} from "@angular/common/http";
import {AppConstants} from "./app.constants";
import {User} from "./user.model";

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  constructor(private http:HttpClient) { }

  getAccountDetails(user : User){
    return this.http.post(environment.rooturl + AppConstants.ACCOUNT_API_URL,user,{ observe: 'response',withCredentials: true });
  }

  saveMessage(contact : Contact){
    return this.http.post(environment.rooturl + AppConstants.CONTACT_API_URL,contact,{ observe: 'response'});
  }

  getBooksDetails(user : User){
    return this.http.post(environment.rooturl + AppConstants.BOOKS_API_URL,user,{ observe: 'response',withCredentials: true });
  }
}
