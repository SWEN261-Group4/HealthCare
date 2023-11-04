import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  toggleDropdown() {
    const icon = document.querySelector('.icon');
    if (icon) {
      icon.classList.toggle('clicked');
    }
  }
}
