import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  enrolledCourses: [],
};

const enrollmentSlice = createSlice({
  name: "enrollment",
  initialState,
  reducers: {
    enrollCourse: (state, action) => {
      if (!state.enrolledCourses.includes(action.payload)) {
        state.enrolledCourses.push(action.payload);
      }
    },
    removeCourse: (state, action) => {
      state.enrolledCourses = state.enrolledCourses.filter(
        (course) => course !== action.payload
      );
    },
  },
});

export const { enrollCourse, removeCourse } = enrollmentSlice.actions;
export default enrollmentSlice.reducer;