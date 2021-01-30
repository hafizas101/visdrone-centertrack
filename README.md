# visdrone-centertrack
This repository holds the code and results for my project titled "Multi-object tracking on drone images". In this project, I have trained CenterTrack network on VisDrone dataset in several experiment settings. Trained models have been evaluated on VisDrone test dev dataset and using [VisDrone MOT Toolkit](https://github.com/VisDrone/VisDrone2018-MOT-toolkit.git). Final results have been plotted and compared with state of the art benchmark results. The video demo of this project is on [YouTube](https://www.youtube.com/watch?v=q1-l-brHvgU&ab_channel=ArslanSiddique) . The below figure shows the qualitative results of our trained model on a test-dev image.
<p align="center">
  <img width="600" height="320" src="https://github.com/hafizas101/visdrone-centertrack/blob/master/images/demo3.jpg">
</p>

## Experiment settings
We perform trainings in 4 different settings utilizing different image resolutions and number of classes. The below figure describes our experiment settings.
<p align="center">
  <img width="450" height="150" src="https://github.com/hafizas101/visdrone-centertrack/blob/master/images/exp_settings.PNG">
</p>

## Results
<p align="center">
  <img width="600" height="320" src="https://github.com/hafizas101/visdrone-centertrack/blob/master/images/mAP_1.PNG">
</p>
<p align="center">
  <img width="600" height="320" src="https://github.com/hafizas101/visdrone-centertrack/blob/master/images/mAP_2.PNG">
</p>
