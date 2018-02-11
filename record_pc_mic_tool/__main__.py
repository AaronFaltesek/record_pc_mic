
def set_config():
    config={"record_prgm_path":"/c/example"}
    return config

def main():
    print("record_pc_mic_tool main!")
    print("Set config")
    config = set_config()
    print(config.__str__())

if __name__ == "__main__":
    main()