Run main.py with the sample video file to generate the test.csv file
python main.py
Run the add_missing_data.py file for interpolation of values to match up for the missing frames and smooth output.
python add_missing_data.py
Finally run the visualize.py passing in the interpolated csv files and hence obtaining a smooth output for license plate detection.
python visualize.py
