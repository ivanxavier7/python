export class Books {

  public id: number | undefined;
  public accountId: number | undefined;
  public author: string | undefined;
  public description: string | undefined;
  public name: string | undefined;
  public price: number | undefined;

  constructor(id?: number,accountId?: number,author?: string,
              description?: string,name?: string, price?: number){
    this.id = id;
    this.accountId = accountId;
    this.author = author;
    this.description = description;
    this.name = name;
    this.price = price;
  }

}
