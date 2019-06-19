

const
    gulp = require('gulp'),
    del = require('del'),
    sass = require('gulp-sass');
browserSync = require('browser-sync').create();
dir = {
    src: 'src/',
    build: 'build/'
};

gulp.task('clean', () => {

    del([dir.build]);
    done();
});

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


gulp.task("browserSync", gulp.series(function () {
    /* other code */
    browserSync.init({
        notify: false,
        port: 8000,
        proxy: 'http://127.0.0.1:8000/'
    });

}));


gulp.task('default', gulp.series('sass', 'browserSync', (done) => {

    // CSS changes
    gulp.watch('holidaydream_project/web/static/web/sass/**/*.scss', gulp.series('sass'));
    gulp.watch('holidaydream_project/web/template/**/*.html');
    done();
}));