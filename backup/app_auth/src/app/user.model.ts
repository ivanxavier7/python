export class User {
  public name: string | undefined;
  public role: string | undefined;
  public email: string | undefined;
  public password: string | undefined;
  public authStatus: string | undefined;
  public statusCd: string | undefined;
  public id: number | undefined;
  public statusMsg: string | undefined;
  public mobileNumber: string | undefined;

  constructor(id?: number, name?: string, mobileNumber?: string, email?: string, password?: string, role?: string,
              statusCd?: string, statusMsg?: string, authStatus?: string) {
    this.name = name;
    this.role = role;
    this.email = email;
    this.password = password;
    this.authStatus = authStatus;
    this.statusCd = statusCd;
    this.id = id;
    this.statusMsg = statusMsg;
    this.mobileNumber = mobileNumber;
  }
}
