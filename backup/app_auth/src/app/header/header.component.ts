import {Component, OnInit} from '@angular/core';
import {User} from "../user.model";
import {KeycloakProfile} from "keycloak-js";
import {KeycloakService} from "keycloak-angular";
import {LoginService} from "../login.service";
import {Subscription} from "rxjs";

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  user = new User();
  public isLoggedIn = false;
  public userProfile: KeycloakProfile | null = null;
  clickEventsubscription: Subscription;

  constructor(private readonly keycloak: KeycloakService, private loginService: LoginService) {
    this.clickEventsubscription = this.loginService.getClickEvent().subscribe(() => {
      console.log("teste")
      this.login();
    })
  }

  public async ngOnInit() {
    this.isLoggedIn = await this.keycloak.isLoggedIn();

    if (this.isLoggedIn) {
      this.userProfile = await this.keycloak.loadUserProfile();
      this.user.authStatus = 'AUTH';
      this.user.name = this.userProfile.firstName;
      window.sessionStorage.setItem("userdetails", JSON.stringify(this.user));

    }
  }

  public login() {
    this.keycloak.login();
  }

  public logout() {
    this.keycloak.logout("http://localhost:4200/login");
  }
}
