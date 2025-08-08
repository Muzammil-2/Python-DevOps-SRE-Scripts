def generate_credential_report():
    iam.generate_credential_report()
    report = iam.get_credential_report()
    with open('iam_credential_report.csv', 'wb') as f:
        f.write(report['Content'])
    print("IAM credential report downloaded as iam_credential_report.csv")

generate_credential_report()
