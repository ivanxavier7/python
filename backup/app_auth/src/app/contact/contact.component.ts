import {Component, OnInit} from '@angular/core';
import {Contact} from "src/app/contact.model";
import {NgForm} from "@angular/forms";
import {DashboardService} from "../dashboard.service";

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {
  model = new Contact();

  constructor(private dashboardService: DashboardService) {
  }

  ngOnInit(): void {
  }

  saveMessage(contactForm: NgForm) {
    this.dashboardService.saveMessage(this.model).subscribe(
      responseData => {
        this.model = <any>responseData.body;
        contactForm.resetForm();
      }, error => {
        console.log(error);
      });
  }
}
