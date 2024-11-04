# Teststand

Für die Durchführung der Messungen wurden fünf Class-D-Verstärkerboards ausge-wählt: TAS5825, TAS2781, TAS2764, SSM3525 und MAX98374. Ziel dieser Messun-gen ist es, die „Big Six“ Parameter – Pegel, Frequenzgang, THD+N, Phase, Überspre-chen und Signal-Rausch-Verhältnis – zu erfassen und zu analysieren. Der Messaufbau nutzt den APx52x B Series Audio Analyzer, der über die APx500 v9.0 Software gesteu-ert wird, um diese Parameter genau zu messen und zu bewerten.

Das Testsignal wird durch den APx52x Audio Analyzer erzeugt und über das I2S-Protokoll (Inter-IC Sound) an die Eingänge der Class-D-Verstärker übertragen. An-schließend werden die verstärkten Ausgangssignale der Boards zurück in den Analyzer geleitet, um die Verstärkerleistung anhand der relevanten Parameter auszuwerten. Eine entscheidende Voraussetzung für den Betrieb der Verstärkerboards ist die Konfiguration einer Startsequenz, die mit der PurePath Console von Texas Instruments erstellt wird und über das I2C-Protokoll (Inter-Integrated Circuit) an die Boards übertragen wird.
 
Abbildung 1: Messaufbau

## Geräte und Protokolle

### Audio Analyzer
Der APx52x Analyzer ist ein präzises Messinstrument, das speziell für Audiotests entwi-ckelt wurde. In Kombination mit der APx500 v9.0 Software ermöglicht er detaillierte und genaue Messungen der „Big Six“ Parameter und ist ein entscheidendes Werkzeug für diese Untersuchungen. Der Analyzer unterstützt verschiedene Signalquellen und Schnitt-stellen und stellt damit eine flexible Lösung für umfassende Audiotests dar.

### I2S-Protokoll
Das I2S (Inter-IC Sound) Protokoll wurde speziell für die Übertragung von Audiosignalen zwischen digitalen Audio-Komponenten entwickelt. Es ermöglicht eine präzise Über-tragung der Audiodaten und bietet die notwendige Synchronisation zwischen den digita-len Audioquellen und den Verstärkern. Die Verwendung des I2S-Protokolls stellt sicher, dass das Testsignal ohne Qualitätseinbußen zu den Eingängen der Class-D-Verstärker gelangt, was entscheidend für die Validität der Messungen ist.

### I2C-Protokol
Das I2C-Protokoll (Inter-Integrated Circuit) dient der Kommunikation zwischen verschie-denen Komponenten, wie in diesem Fall zwischen der PurePath Console und den Ver-stärkerboards. Es ermöglicht eine einfache Konfiguration und Steuerung der Geräte über eine serielle Schnittstelle. Im Rahmen dieser Messung wird das I²C-Protokoll zur Über-tragung der Startsequenz verwendet, die notwendig ist, um die Boards für den Messbe-trieb zu initialisieren.

## Startsequenz
Die Startsequenz ist erforderlich, um die Verstärkerboards in den korrekten Betriebszu-stand zu versetzen. Diese Sequenz umfasst Konfigurationsbefehle, die den Betrieb der Class-D-Verstärker auf die gewünschte Leistung und Effizienz einstellen. Die PurePath Console von Texas Instruments wird verwendet, um die Startsequenz präzise zu definie-ren, bevor sie über das I²C-Protokoll an die Boards gesendet wird. Die Implementierung der Startsequenz gewährleistet, dass die Boards stabil und korrekt arbeiten, was entschei-dend für die anschließende Messung der „Big Six“ Parameter ist. 

## Durchführung der Messungen
Sobald die Startsequenz abgeschlossen und die Boards betriebsbereit sind, wird der APx52x Analyzer verwendet, um ein standardisiertes Testsignal zu erzeugen. Dieses Sig-nal wird über das I²S-Protokoll an die Eingänge der Class-D-Verstärkerboards übertra-gen. Die Ausgänge der Verstärker werden wiederum mit dem Analyzer verbunden, um die „Big Six“ Parameter detailliert zu messen und zu analysieren.
