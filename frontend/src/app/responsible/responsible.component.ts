import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-responsible',
  templateUrl: './responsible.component.html',
  styleUrls: ['./responsible.component.css']
})
export class ResponsibleComponent {
  email: string = '';
  message: string = '';

  constructor(private router: Router) { }

  validateInputs() {
    if (this.email.trim() !== '') {
      localStorage.setItem('responsibleEmail', this.email);
      localStorage.setItem('responsibleMessage', this.message);
      this.router.navigate(['/file-upload']);
    } else {
      alert('Please enter a valid email.');
    }
  }
}
