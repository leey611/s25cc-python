# Sardine Basics
- [Synths and samples](https://sardine.raphaelforment.fr/getting_started/samples_and_synths.html)
- [Patterns](https://sardine.raphaelforment.fr/getting_started/patterns.html)


## Synatax
The following code assigns the pattern to a player called `Pa`
```
Pa >> d('bd cp .')
```
- `Pa`: a player called `Pa`, you can see this as a track, and can have other players, such as `Pb`, `Pc`
- `>>` or `*`: `>>` means assign a pattern to a player; `*` means modify a player's pattern live instead of restarting
- `d()`: a function where we put a drum pattern
- `.`: rest

### Common sounds
[list of default samples](https://sardine.raphaelforment.fr/getting_started/samples_and_synths.html)
| Shortcode | Stands for |
|:----------|:-----------|
| bd        | Bass Drum  | 
| cp        | Clap       | 
| hh        | Hi-Hat     | 
| sn        | Snare      | 

## Patterns
[reference](https://sardine.raphaelforment.fr/getting_started/patterns.html)

### Parameters
[list of parameters](https://sardine.raphaelforment.fr/audio_engine/sampler.html)
```
Pa * d('reverbkick east:4 yeah:2 mt', speed=1.2, shape=0.5, p=0.5) 
Pa * d('reverbkick east:4 yeah:2 mt', speed='1.2 2', shape=0.5, p='0.5 0.25')
Pa * d('reverbkick east:4 yeah:2 mt cr', speed='1.2 2.2', shape=0.7, p='0.5!2 0.25!5')

silence(Pa)
```

### Multiple players
```
Pa * d('bd cp', p=1) # plays every beat, alternating bd and cp
Pb * d('hh27:2', p=0.5) # plays every 1/2 beat
Pc * d('. east:4!2 .', p=0.25) # plays 2nd and 3rd of the 1/4 beat
Pd * d('. . . bleep:0', p=0.25) # plays every 4th of the 1/4 beat

silence()
```