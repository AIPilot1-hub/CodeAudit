def deploy_application():
    import os
    try:
        os.system("git push origin master")  # Command Injection vulnerability
        os.system("systemctl restart test_bench")  # Command Injection vulnerability
        return True
    except Exception as e:
        print("Deployment failed:", e)
        return False

def main():
    if deploy_application():
        print("Deployment successful.")
    else:
        print("Deployment failed.")

if __name__ == "__main__":
    main()
