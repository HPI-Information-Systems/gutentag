# GutenTAG
A good **T**imeseries **A**nomaly **G**enerator.

## Usage

```python
from gutenTAG.generator import GutenTAG
```


## Structure

### Base Oscillations
The generator comes with the following base oscillations in [./gutenTAG/base_oscillations](./gutenTAG/base_oscillations):

- sinus
- random walk
- cylinder bell funnel
- synthetic ecg
- CoMuT

#### Usage

```python
from gutenTAG.base_oscillations import BaseOscillation

options = {
    # ...
}

# to generate a sinus oscillation without anomalies
BaseOscillation.Sinus(**options).generate()
```

### Anomalies
Also, the generator comes with the following anomaly types in [./gutenTAG/anomalies/types](./gutenTAG/anomalies/types):

- extremum
- frequency
- mean
- pattern
- pattern_shift
- platform
- variance

#### Usage

```python
from gutenTAG.base_oscillations import BaseOscillation
from gutenTAG.anomalies import Anomaly, Position
from gutenTAG.anomalies.types.platform import AnomalyPlatform

options = {
    # ...
}

anomalies = [
    Anomaly(Position.Beginning, anomaly_length=200).set_platform(AnomalyPlatform(0.0))
]

# to generate a sinus oscillation with a platform anomaly
BaseOscillation.Sinus(**options).inject_anomalies(anomalies).generate()
```