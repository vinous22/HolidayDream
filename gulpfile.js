(function () {
    var gulp = require('gulp');
    var sass = require('gulp-sass');
    var browserSync = require('browser-sync').create();
    var exec = require('child_process').exec;

    gulp.task('sass', function () {
        return gulp.src('holidaydream_project/web/static/web/sass/**/*.scss')
            .pipe(sass()).on('error', function (err) {
                console.log(err.toString());
                this.emit('end');
            })
            .pipe(gulp.dest('holidaydream_project/web/static/web/css'))
            .pipe(browserSync.reload({
                stream: true
            }));
    });

    gulp.task('browserSync', function () {
        browserSync.init({
            notify: false,
            port: 8000,
            proxy: 'http://127.0.0.1:8000/'
        });
    });

    gulp.task('default', ['browserSync', 'sass'], function () {
        gulp.watch('holidaydream_project/web/static/web/sass/**/*.scss', ['sass']).on('change', browserSync.reload);
        gulp.watch('holidaydream_project/web/static/web/js/*.js').on('change', browserSync.reload);
        gulp.watch('holidaydream_project/web/template/**/*.html').on('change', browserSync.reload);
    });

})();