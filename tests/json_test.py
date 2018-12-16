from src.json_parser import JsonReader

if __name__ == "__main__":

    json_test = JsonReader()
    json_test.read_from_file("../data/aruco_params.json")
    json_test.print_json()

    print(json_test.get_value("marker_type"))
    print(json_test.get_value("features"))
    print(json_test.get_value("feature_count"))