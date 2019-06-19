// const { series } = require('gulp');
var gulp = require('gulp');
var sass = require('gulp-sass');
var browserSync = require('browser-sync').create();


gulp.task("sass", gulp.series(function () {
    /* other code */
    return gulp.src('holidaydream_project/web/static/web/sass/**/*.scss')
        .pipe(sass()).on('error', function (err) {
            console.log(err.toString());
            this.emit('end');
        })
        .pipe(gulp.dest('holidaydream_project/web/static/web/css'))
        .pipe(browserSync.reload({
            stream: true
        }));
}));


// gulp.task("browserSync", gulp.series(function () {
//     /* other code */
//     browserSync.init({
//         notify: false,
//         port: 8000,
//         proxy: 'http://127.0.0.1:8000/'
//     });
// }));


// gulp.watch("web/static/sass/**/*.scss", ["sass"]);
// gulp.watch("web/static/js/*.js", ["js"]);
// gulp.watch("web/**/templates/**/*.html", ["js"]);

// gulp.task('default', gulp.series('sass', 'browserSync'));



gulp.task('build', gulp.parallel('sass'));
gulp.task('default', gulp.parallel('build'));