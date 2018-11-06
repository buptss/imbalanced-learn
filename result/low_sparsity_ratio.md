/Library/Python/2.7/site-packages/sklearn/metrics/classification.py:1143: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 due to no predicted samples.
  'precision', 'predicted', average, warn_for)
/Library/Python/2.7/site-packages/sklearn/metrics/classification.py:1143: UndefinedMetricWarning: F-score is ill-defined and being set to 0.0 due to no predicted samples.
  'precision', 'predicted', average, warn_for)
\multirow{6}{*}{\textbf{ecoli}}
&ADASYN& 0.907& 0.547& 0.588& \textbf{0.909}& 0.714& 0.907\\
&No Sample& 0.850& 0.618& \textbf{0.800}& 0.727& 0.762& 0.841\\
&SMOTE& 0.913& 0.580& 0.625& \textbf{0.909}& 0.741& 0.913\\
&SMOTEBorderline-1& \textbf{0.927}& \textbf{0.661}& 0.714& \textbf{0.909}& \textbf{0.800}& \textbf{0.927}\\
&SMOTEBorderline-2& 0.907& 0.547& 0.588& \textbf{0.909}& 0.714& 0.907\\
&SVMSMOTE& \textbf{0.927}& \textbf{0.661}& 0.714& \textbf{0.909}& \textbf{0.800}& \textbf{0.927}\\
&Sparse SMOTE& 0.913& 0.580& 0.625& \textbf{0.909}& 0.741& 0.913\\
&random& 0.920& 0.618& 0.667& \textbf{0.909}& 0.769& 0.920\\
\hline
\multirow{6}{*}{\textbf{optical_digits}}
&ADASYN& 0.921& 0.681& 0.767& 0.871& 0.816& 0.920\\
&No Sample& 0.824& 0.664& \textbf{0.968}& 0.650& 0.778& 0.805\\
&SMOTE& 0.927& \textbf{0.756}& 0.853& 0.871& \textbf{0.862}& 0.926\\
&SMOTEBorderline-1& 0.901& 0.733& 0.877& 0.814& 0.844& 0.897\\
&SMOTEBorderline-2& 0.898& 0.737& 0.890& 0.807& 0.846& 0.893\\
&SVMSMOTE& 0.902& 0.639& 0.745& 0.836& 0.788& 0.900\\
&Sparse SMOTE& 0.925& 0.731& 0.824& 0.871& 0.847& 0.924\\
&random& \textbf{0.932}& 0.704& 0.776& \textbf{0.893}& 0.831& \textbf{0.931}\\
\hline
\multirow{6}{*}{\textbf{satimage}}
&ADASYN& \textbf{0.882}& 0.381& 0.416& \textbf{0.893}& 0.567& \textbf{0.882}\\
&No Sample& 0.684& 0.333& \textbf{0.722}& 0.383& 0.500& 0.614\\
&SMOTE& 0.866& \textbf{0.420}& 0.492& 0.819& \textbf{0.615}& 0.865\\
&SMOTEBorderline-1& 0.872& 0.376& 0.420& 0.866& 0.566& 0.872\\
&SMOTEBorderline-2& 0.865& 0.377& 0.429& 0.846& 0.569& 0.865\\
&SVMSMOTE& 0.867& 0.393& 0.451& 0.839& 0.587& 0.867\\
&Sparse SMOTE& 0.849& 0.405& 0.494& 0.779& 0.604& 0.846\\
&random& 0.877& 0.412& 0.467& 0.852& 0.603& 0.876\\
\hline
\multirow{6}{*}{\textbf{pen_digits}}
&ADASYN& 0.937& 0.803& 0.895& 0.885& 0.890& 0.936\\
&No Sample& 0.881& 0.774& \textbf{0.985}& 0.762& 0.860& 0.873\\
&SMOTE& 0.951& 0.856& 0.933& 0.908& 0.920& 0.950\\
&SMOTEBorderline-1& 0.948& 0.815& 0.888& 0.908& 0.898& 0.947\\
&SMOTEBorderline-2& 0.912& 0.712& 0.827& 0.843& 0.835& 0.910\\
&SVMSMOTE& \textbf{0.956}& 0.808& 0.864& \textbf{0.927}& 0.895& \textbf{0.956}\\
&Sparse SMOTE& 0.948& \textbf{0.870}& 0.955& 0.900& \textbf{0.927}& 0.947\\
&random& 0.953& 0.843& 0.912& 0.916& 0.914& 0.952\\
\hline
\multirow{6}{*}{\textbf{abalone}}
&ADASYN& 0.753& 0.200& 0.237& \textbf{0.747}& 0.359& 0.753\\
&No Sample& 0.500& 0.091& 0.000& 0.000& 0.000& 0.000\\
&SMOTE& 0.753& 0.205& 0.248& 0.726& 0.370& 0.753\\
&SMOTEBorderline-1& 0.742& 0.200& 0.248& 0.695& 0.366& 0.741\\
&SMOTEBorderline-2& 0.750& \textbf{0.214}& 0.271& 0.684& \textbf{0.388}& 0.747\\
&SVMSMOTE& 0.741& 0.211& \textbf{0.276}& 0.653& 0.387& 0.735\\
&Sparse SMOTE& 0.742& 0.203& 0.255& 0.684& 0.371& 0.740\\
&random& \textbf{0.754}& 0.203& 0.243& 0.737& 0.366& \textbf{0.753}\\
\hline
\multirow{6}{*}{\textbf{sick_euthyroid}}
&ADASYN& \textbf{0.949}& 0.741& 0.800& \textbf{0.918}& 0.855& \textbf{0.949}\\
&No Sample& 0.930& \textbf{0.778}& \textbf{0.883}& 0.869& \textbf{0.876}& 0.928\\
&SMOTE& \textbf{0.949}& 0.741& 0.800& \textbf{0.918}& 0.855& \textbf{0.949}\\
&SMOTEBorderline-1& \textbf{0.949}& 0.741& 0.800& \textbf{0.918}& 0.855& \textbf{0.949}\\
&SMOTEBorderline-2& \textbf{0.949}& 0.741& 0.800& \textbf{0.918}& 0.855& \textbf{0.949}\\
&SVMSMOTE& 0.949& 0.730& 0.789& \textbf{0.918}& 0.848& 0.948\\
&Sparse SMOTE& 0.941& 0.726& 0.797& 0.902& 0.846& 0.940\\
&random& \textbf{0.949}& 0.741& 0.800& \textbf{0.918}& 0.855& \textbf{0.949}\\
\hline
\multirow{6}{*}{\textbf{spectrometer}}
&ADASYN& \textbf{0.929}& \textbf{0.820}& 0.929& \textbf{0.867}& \textbf{0.897}& \textbf{0.927}\\
&No Sample& \textbf{0.929}& \textbf{0.820}& 0.929& \textbf{0.867}& \textbf{0.897}& \textbf{0.927}\\
&SMOTE& 0.896& 0.761& 0.923& 0.800& 0.857& 0.891\\
&SMOTEBorderline-1& 0.867& 0.763& \textbf{1.000}& 0.733& 0.846& 0.856\\
&SMOTEBorderline-2& 0.883& 0.623& 0.750& 0.800& 0.774& 0.879\\
&SVMSMOTE& \textbf{0.929}& \textbf{0.820}& 0.929& \textbf{0.867}& \textbf{0.897}& \textbf{0.927}\\
&Sparse SMOTE& \textbf{0.929}& \textbf{0.820}& 0.929& \textbf{0.867}& \textbf{0.897}& \textbf{0.927}\\
&random& 0.925& 0.766& 0.867& \textbf{0.867}& 0.867& 0.923\\
\hline
\multirow{6}{*}{\textbf{isolet}}
&ADASYN& 0.910& 0.560& 0.642& 0.857& 0.734& 0.909\\
&No Sample& 0.709& 0.424& \textbf{0.908}& 0.421& 0.576& 0.648\\
&SMOTE& \textbf{0.950}& \textbf{0.636}& 0.675& \textbf{0.936}& \textbf{0.784}& \textbf{0.950}\\
&SMOTEBorderline-1& 0.896& 0.540& 0.637& 0.829& 0.720& 0.894\\
&SMOTEBorderline-2& 0.916& 0.503& 0.559& 0.886& 0.685& 0.915\\
&SVMSMOTE& 0.933& 0.520& 0.558& 0.921& 0.695& 0.932\\
&Sparse SMOTE& 0.945& 0.575& 0.609& \textbf{0.936}& 0.738& 0.945\\
&random& 0.944& 0.569& 0.604& \textbf{0.936}& 0.734& 0.944\\
\hline
\multirow{6}{*}{\textbf{us_crime}}
&ADASYN& 0.844& 0.387& 0.478& \textbf{0.767}& 0.589& 0.841\\
&No Sample& 0.658& 0.311& \textbf{0.778}& 0.326& 0.459& 0.568\\
&SMOTE& 0.812& 0.353& 0.469& 0.698& 0.561& 0.804\\
&SMOTEBorderline-1& 0.812& 0.404& 0.558& 0.674& 0.611& 0.800\\
&SMOTEBorderline-2& 0.825& 0.379& 0.492& 0.721& 0.585& 0.819\\
&SVMSMOTE& 0.813& 0.412& 0.569& 0.674& 0.617& 0.801\\
&Sparse SMOTE& 0.799& 0.381& 0.538& 0.651& 0.589& 0.785\\
&random& \textbf{0.852}& \textbf{0.429}& 0.532& \textbf{0.767}& \textbf{0.629}& \textbf{0.848}\\
\hline
\multirow{6}{*}{\textbf{yeast_ml8}}
&ADASYN& 0.490& 0.067& 0.038& 0.024& 0.030& 0.153\\
&No Sample& 0.500& 0.068& 0.000& 0.000& 0.000& 0.000\\
&SMOTE& 0.511& 0.070& 0.118& 0.049& 0.069& 0.218\\
&SMOTEBorderline-1& \textbf{0.550}& \textbf{0.085}& 0.188& 0.146& \textbf{0.164}& 0.374\\
&SMOTEBorderline-2& 0.515& 0.071& 0.111& 0.073& 0.088& 0.265\\
&SVMSMOTE& 0.509& 0.071& \textbf{0.200}& 0.024& 0.043& 0.156\\
&Sparse SMOTE& 0.533& 0.073& 0.091& \textbf{0.244}& 0.132& \textbf{0.448}\\
&random& 0.495& 0.068& 0.000& 0.000& 0.000& 0.000\\
\hline
\multirow{6}{*}{\textbf{scene}}
&ADASYN& 0.581& 0.109& 0.186& 0.265& 0.218& 0.488\\
&No Sample& 0.509& 0.090& \textbf{0.500}& 0.020& 0.039& 0.143\\
&SMOTE& 0.606& 0.131& 0.255& 0.286& 0.269& 0.514\\
&SMOTEBorderline-1& 0.563& 0.103& 0.189& 0.204& 0.196& 0.434\\
&SMOTEBorderline-2& 0.615& 0.137& 0.263& 0.306& 0.283& 0.532\\
&SVMSMOTE& 0.589& 0.121& 0.245& 0.245& 0.245& 0.478\\
&Sparse SMOTE& 0.591& 0.118& 0.220& 0.265& 0.241& 0.493\\
&random& \textbf{0.630}& \textbf{0.144}& 0.262& \textbf{0.347}& \textbf{0.298}& \textbf{0.563}\\
\hline
\multirow{6}{*}{\textbf{libras_move}}
&ADASYN& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}\\
&No Sample& 0.750& 0.511& \textbf{1.000}& 0.500& 0.667& 0.707\\
&SMOTE& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}\\
&SMOTEBorderline-1& 0.994& 0.667& 0.667& \textbf{1.000}& 0.800& 0.994\\
&SMOTEBorderline-2& 0.989& 0.500& 0.500& \textbf{1.000}& 0.667& 0.989\\
&SVMSMOTE& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}\\
&Sparse SMOTE& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}& \textbf{1.000}\\
&random& 0.994& 0.667& 0.667& \textbf{1.000}& 0.800& 0.994\\
\hline
\multirow{6}{*}{\textbf{thyroid_sick}}
&ADASYN& 0.941& 0.754& 0.833& 0.896& 0.863& 0.940\\
&No Sample& 0.886& 0.750& \textbf{0.945}& 0.776& 0.852& 0.879\\
&SMOTE& 0.941& 0.764& 0.845& 0.896& 0.870& 0.940\\
&SMOTEBorderline-1& 0.933& 0.740& 0.831& 0.881& 0.855& 0.932\\
&SMOTEBorderline-2& 0.926& 0.727& 0.829& 0.866& 0.847& 0.924\\
&SVMSMOTE& 0.941& 0.764& 0.845& 0.896& 0.870& 0.940\\
&Sparse SMOTE& 0.961& 0.754& 0.797& \textbf{0.940}& 0.863& 0.961\\
&random& \textbf{0.963}& \textbf{0.784}& 0.829& \textbf{0.940}& \textbf{0.881}& \textbf{0.962}\\
\hline
\multirow{6}{*}{\textbf{oil}}
&ADASYN& 0.793& 0.236& 0.357& \textbf{0.625}& 0.455& 0.775\\
&No Sample& 0.683& 0.246& \textbf{0.600}& 0.375& 0.462& 0.610\\
&SMOTE& 0.793& 0.236& 0.357& \textbf{0.625}& 0.455& 0.775\\
&SMOTEBorderline-1& \textbf{0.804}& \textbf{0.360}& 0.556& \textbf{0.625}& \textbf{0.588}& \textbf{0.784}\\
&SMOTEBorderline-2& 0.793& 0.236& 0.357& \textbf{0.625}& 0.455& 0.775\\
&SVMSMOTE& \textbf{0.804}& \textbf{0.360}& 0.556& \textbf{0.625}& \textbf{0.588}& \textbf{0.784}\\
&Sparse SMOTE& 0.728& 0.160& 0.286& 0.500& 0.364& 0.691\\
&random& 0.737& 0.217& 0.400& 0.500& 0.444& 0.698\\
\hline
\multirow{6}{*}{\textbf{wine_quality}}
&ADASYN& 0.715& \textbf{0.128}& 0.219& 0.500& 0.305& 0.682\\
&No Sample& 0.510& 0.048& \textbf{0.500}& 0.022& 0.042& 0.147\\
&SMOTE& 0.714& 0.126& 0.215& 0.500& 0.301& 0.681\\
&SMOTEBorderline-1& 0.669& 0.109& 0.220& 0.391& 0.281& 0.608\\
&SMOTEBorderline-2& \textbf{0.716}& 0.115& 0.186& \textbf{0.522}& 0.274& \textbf{0.689}\\
&SVMSMOTE& 0.666& 0.127& 0.279& 0.370& \textbf{0.318}& 0.596\\
&Sparse SMOTE& 0.687& 0.116& 0.217& 0.435& 0.290& 0.639\\
&random& 0.695& 0.117& 0.212& 0.457& 0.290& 0.653\\
\hline
\multirow{6}{*}{\textbf{letter_img}}
&ADASYN& \textbf{0.970}& 0.563& 0.580& \textbf{0.970}& 0.726& \textbf{0.970}\\
&No Sample& 0.856& \textbf{0.710}& \textbf{0.979}& 0.714& \textbf{0.826}& 0.844\\
&SMOTE& 0.954& 0.602& 0.645& 0.930& 0.761& 0.954\\
&SMOTEBorderline-1& 0.832& 0.422& 0.599& 0.683& 0.638& 0.819\\
&SMOTEBorderline-2& 0.876& 0.438& 0.552& 0.779& 0.646& 0.871\\
&SVMSMOTE& 0.958& 0.484& 0.505& 0.955& 0.661& 0.958\\
&Sparse SMOTE& 0.952& 0.604& 0.650& 0.925& 0.763& 0.952\\
&random& 0.970& 0.593& 0.613& 0.965& 0.750& 0.970\\
\hline
\multirow{6}{*}{\textbf{yeast_me2}}
&ADASYN& 0.811& 0.148& 0.200& 0.700& 0.311& 0.804\\
&No Sample& 0.697& \textbf{0.283}& \textbf{0.667}& 0.400& \textbf{0.500}& 0.631\\
&SMOTE& 0.817& 0.166& 0.226& 0.700& 0.341& 0.808\\
&SMOTEBorderline-1& 0.822& 0.190& 0.259& 0.700& 0.378& 0.813\\
&SMOTEBorderline-2& 0.860& 0.178& 0.216& \textbf{0.800}& 0.340& 0.858\\
&SVMSMOTE& 0.776& 0.167& 0.261& 0.600& 0.364& 0.756\\
&Sparse SMOTE& \textbf{0.871}& 0.226& 0.276& \textbf{0.800}& 0.410& \textbf{0.868}\\
&random& 0.861& 0.183& 0.222& \textbf{0.800}& 0.348& 0.859\\
\hline
\multirow{6}{*}{\textbf{ozone_level}}
&ADASYN& 0.775& 0.144& 0.225& 0.600& 0.327& 0.755\\
&No Sample& 0.500& 0.024& 0.000& 0.000& 0.000& 0.000\\
&SMOTE& 0.778& 0.159& 0.250& 0.600& 0.353& 0.758\\
&SMOTEBorderline-1& 0.723& 0.176& 0.350& 0.467& 0.400& 0.676\\
&SMOTEBorderline-2& 0.782& 0.184& 0.290& 0.600& 0.391& 0.761\\
&SVMSMOTE& 0.658& 0.120& 0.312& 0.333& 0.323& 0.572\\
&Sparse SMOTE& 0.746& 0.137& 0.235& 0.533& 0.327& 0.715\\
&random& \textbf{0.819}& \textbf{0.246}& \textbf{0.357}& \textbf{0.667}& \textbf{0.465}& \textbf{0.805}\\
\hline
\multirow{6}{*}{\textbf{mammography}}
&ADASYN& \textbf{0.909}& 0.297& 0.344& \textbf{0.855}& 0.491& \textbf{0.907}\\
&No Sample& 0.732& \textbf{0.378}& \textbf{0.784}& 0.468& \textbf{0.586}& 0.683\\
&SMOTE& 0.882& 0.330& 0.412& 0.790& 0.541& 0.878\\
&SMOTEBorderline-1& 0.885& 0.277& 0.338& 0.806& 0.476& 0.882\\
&SMOTEBorderline-2& 0.886& 0.188& 0.220& 0.839& 0.349& 0.884\\
&SVMSMOTE& 0.885& 0.279& 0.340& 0.806& 0.478& 0.882\\
&Sparse SMOTE& 0.905& 0.334& 0.394& 0.839& 0.536& 0.902\\
&random& 0.888& 0.307& 0.376& 0.806& 0.513& 0.884\\
\hline
\multirow{6}{*}{\textbf{protein_homo}}
&ADASYN& \textbf{0.947}& 0.237& 0.257& \textbf{0.917}& 0.402& \textbf{0.946}\\
&No Sample& 0.850& \textbf{0.681}& \textbf{0.970}& 0.699& \textbf{0.813}& 0.836\\
&SMOTE& 0.941& 0.341& 0.380& 0.896& 0.533& 0.940\\
&SMOTEBorderline-1& 0.930& 0.313& 0.357& 0.874& 0.507& 0.928\\
&SMOTEBorderline-2& 0.936& 0.278& 0.312& 0.890& 0.462& 0.935\\
&SVMSMOTE& 0.927& 0.410& 0.475& 0.862& 0.612& 0.924\\
&Sparse SMOTE& 0.940& 0.267& 0.297& 0.899& 0.446& 0.939\\
&random& 0.939& 0.351& 0.394& 0.890& 0.546& 0.937\\
\hline
\multirow{6}{*}{\textbf{abalone_19}}
&ADASYN& 0.453& 0.006& 0.000& 0.000& 0.000& 0.000\\
&No Sample& 0.500& 0.006& 0.000& 0.000& 0.000& 0.000\\
&SMOTE& 0.451& 0.006& 0.000& 0.000& 0.000& 0.000\\
&SMOTEBorderline-1& 0.481& 0.006& 0.000& 0.000& 0.000& 0.000\\
&SMOTEBorderline-2& 0.561& 0.008& \textbf{0.021}& 0.167& \textbf{0.038}& 0.399\\
&SVMSMOTE& 0.486& 0.006& 0.000& 0.000& 0.000& 0.000\\
&Sparse SMOTE& 0.461& 0.006& 0.000& 0.000& 0.000& 0.000\\
&random& \textbf{0.618}& \textbf{0.010}& 0.019& \textbf{0.333}& 0.036& \textbf{0.548}\\
\hline
