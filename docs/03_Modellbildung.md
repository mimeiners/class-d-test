# Modellbildung

## Ziel und Zweck der Modellbildung
Das Ziel der Erstellung des Behavioral Modells eines Class-D-Verstärkers besteht darin, den grundsätzlichen Aufbau und die Funktionsweise eines solchen Verstärkers umfassend zu verstehen. Durch das Modell sollen die wesentlichen Bauelemente und der Betrieb eines Class-D-Verstärkers nachvollziehbar werden, insbesondere wie der Verstärker durch das Ein- und Ausschalten der Transistoren in hoher Effizienz arbeitet und den Leistungsverlust minimiert.
In dieser Arbeit wird das Modell genutzt, um detaillierte Analysen der Verstärkereigenschaften wie Pegel, Frequenzgang, Total Harmonic Distortion plus Noise (THD+N), Phase, Übersprechen und Signal-Rausch-Verhältnis (SNR) durchzuführen.

Das Modell wird zudem dazu eingesetzt, verschiedene Verstärkertypen – TAS2781, TAS2764, SSM3525 und MAX98374 – zu testen und miteinander zu vergleichen. Ziel ist es, die für den Einsatz im Audiosignalpfad der Decoder-Encoder-Unit (DEU) des A320 optimalen Verstärker auszuwählen, wobei die Analyse die Auswahl des für die Digitalisierung und Verstärkung geeigneten Class-D-Verstärkers stützt.

## Beschreibung der Modellannahmen
Ein Class-D-Verstärker besteht aus mehreren essenziellen Funktionsblöcken, die das Eingangssignal effizient verstärken. Zunächst wird das analoge Audiosignal in der Eingangsstufe vorbereitet. Dann wandelt der Modulator das Signal in ein PWM-Signal um, indem er das Audiosignal mit einem Dreieck- oder Sägezahnsignal vergleicht. Die Treiberstufe übernimmt das PWM-Signal und steuert die MOSFETs der Leistungsstufe an, die im H-Brückenformat aufgebaut ist. Diese schalten abwechselnd vollständig ein und aus, wodurch die Energieverluste minimiert werden. Das PWM-Signal wird dann durch einen Tiefpassfilter geleitet, der die hochfrequenten Anteile entfernt und das Signal in eine analoge Form zurückführt, die für den Lautsprecher geeignet ist. Schließlich sorgt eine Feedback-Schleife in manchen Verstärkern dafür, dass das Ausgangssignal möglichst verzerrungsfrei bleibt und das Eingangssignal präzise wiedergegeben wird.
Zur Vereinfachung des Modells werden mehrere Annahmen getroffen. Es wird nur der Ausgang der Eingangsstufe betrachtet, wobei die Spannungsquelle als ideal angenommen wird, um Schwankungen und Störungen in der Versorgungsspannung auszuschließen. Die Treiberstufe wird ebenfalls als ideal modelliert, sodass keine Verluste oder Verzögerungen in der Signalübertragung berücksichtigt werden. Die MOSFETs agieren in diesem Modell als ideale Schalter, die ohne Verluste oder Verzögerungen zwischen den Zuständen „Ein“ und „Aus“ wechseln. Zudem wird die Feedback-Schleife ignoriert, was eine konstante Verstärkung ohne Rückkopplung zur Folge hat.

## Mathematische Modellierung und Gleichungen

### Pulsweitenmodulation (PWM)

### Schaltverhalten der Transistoren
Ein Class-D-Verstärker wandelt das analoge Eingangssignal in ein PWM-Signal um, das die Schalttransistoren ansteuert. Die Modulation basiert auf dem Vergleich des Audiosignals $V_{in}(t)$ mit einer Trägerschwingung, meist einer Dreieck- oder Sägezahnspannung $V_{tr}(t)$. Die PWM-Spannung $V_{PWM}(t)$ kann mathematisch als ein binäres Signal beschrieben werden, das den Zustand der Transistoren steuert:


### Low-Pass-Filter

## Simulation und Implementierung im Simulationstool

## Verifikation und Validierung des Modells

## Diskussion der Modellergebnisse
