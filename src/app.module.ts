import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router'; // Import RouterModule
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UserHomepageComponent } from './user-homepage/user-homepage.component';
import { HealthLoggerComponent } from './health-logger/health-logger.component'; // Import Health Logger component
import { MedicationComponent } from './medication/medication.component'; // Import Medication component
import { AppointmentsComponent } from './appointments/appointments.component'; // Import Appointments component

@NgModule({
  declarations: [
    AppComponent,
    UserHomepageComponent,
    HealthLoggerComponent, // Add Health Logger component to declarations
    MedicationComponent, // Add Medication component to declarations
    AppointmentsComponent, // Add Appointments component to declarations
  ],
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule.forRoot([
      // Configure routes
      { path: 'user-homepage', component: UserHomepageComponent },
      { path: 'health-logger', component: HealthLoggerComponent },
      { path: 'medication', component: MedicationComponent },
      { path: 'appointments', component: AppointmentsComponent },
    ]),
    AppRoutingModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
