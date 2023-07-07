# Theater Work

  


## Introduction

The Flatiron Theater Company is holding auditions!

An actor may only `Audition` for one `Role`, while a `Role` may have many
`Auditions` for it!

![one to many](https://curriculum-content.s3.amazonaws.com/phase-3/active-record-theater-work/one_to_many.png)


## Setup

`pipenv install` will make sure we have ipdb included in our environment.  
`pipenv shell` allows us access to that environment.  


## Getting started


- `Auditions` should have an actor (string), location (string), hired (boolean) and **belong to** a role.
- `Roles` should only have a character_name (string) and **have many** auditions.

## Relationship

- What relationships will this need (i.e. one-to-one, one-to-many, and
  many-to-many)?

## A note about notation

- When you see a `"#"` the functionality is related to the instance, a `"."` the class.

## Testing

- You can now view all of your Python files for your models in the lib folder. They will be automagically available for you so long as you use the `python debug.py` instruction to test your code.

- Through this `debug.py` file, we've provided to you a console that you can use to test your code. To enter a console session, run `python debug.py` from the command line. You'll be able to test out the functionality that you write there.



## Audition

- `Audition#role` returns an instance of role associated with this audition.
- `Audition#call_back()` will change the the hired attribute to `True`.

## Roles

- `Role#auditions` returns all of the auditions associated with this role.
- `Role#actors` returns a list of names from the actors associated with this
  role.
- `Role#locations` returns a list of locations from the auditions associated
  with this role.
- `Role#lead` returns the first instance of the audition that was hired for
  this role or returns a string 'no actor has been hired for this role'.
- `Role#understudy` returns the second instance of the audition that was hired
  for this role or returns a string 'no actor has been hired for understudy for
  this role'.
