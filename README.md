# Refactoring exercise

The code presented in this exercise aims to query data from a CSV file 
containing music tracks, albums, and artists. It works, but it smells quite 
bad! It is intentionally bad: poor naming, improper use of methods, code 
duplication, no consistent code-style, etc. We have included some tests too, 
which will guide you through the exercise and ensure that the interface and 
functionality remain intact.

## Instructions

The exercise involves three assignments. The third one is optional. You are 
free to use any version of python you want, preferably the latest one. You are 
allowed to use third-party libraries. If you do, please include a short 
explanation per library on why you decided to use it.

1. Refactor the `MusicTracks` class in `music_tracks.py`. Keep the following 
points in mind.
    * The code should be readable.
    * The code should be maintainable.
    * The included tests must pass. 

2. Add a new method to the `MusicTracks` class to obtain the top-10 most 
listened tracks.

3. [Bonus] Add any other functionality you may find of interest.

The final goal of this exercise is that you can give your take on the current 
implementation in a way that you can feel proud of the outcome. Feel free to 
create new classes, helper methods, split things into modules, or any other 
modification you may find fit for the exercise. Although we don't expect you 
to, you can even refactor the tests, as long as they keep checking the 
correctness of the code.

## Run the tests
In the console, just type: `python tests.py`

If nothing is returned, everything is ok!
