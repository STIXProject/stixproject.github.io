If possible, an indicator should include the following fields:

* Either Observable, Observable Composition, or Indicator Composition to represent the detectable pattern
* Title
* Type
* Valid_Time_Position
* Indicated_TTP, even if pointing to a very simple TTP with just a title
* A confidence assertion

### Creating pattern observables for indicators
When creating observables for use as patterns within indicators, you should always set the condition attribute on all possible fields to an appropriate value, even if that value is equals. Leaving off the condition attribute implies that the observable is an instance rather than a pattern.
