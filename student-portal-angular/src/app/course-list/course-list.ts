import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CourseCardComponent } from '../course-card/course-card';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [CommonModule, FormsModule, CourseCardComponent],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseListComponent {

  searchTerm = '';

  courses = [
    { name: 'Database Systems', code: 'CS301', credits: 4, grade: 'A' },
    { name: 'Operating Systems', code: 'CS302', credits: 3, grade: 'A+' },
    { name: 'Computer Networks', code: 'CS303', credits: 3, grade: 'B+' },
    { name: 'Web Development', code: 'CS304', credits: 4, grade: 'A' }
  ];

  get filteredCourses() {
    return this.courses.filter(course =>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }

  trackByCode(index: number, course: any) {
    return course.code;
  }

}