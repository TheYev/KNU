# lab-1-mdt
- **Modern database technologies**

## Сondition

- The minimum number of entities is 15.
- Entities must take into account the passage of time, ensure the preservation of some historical ones data, some entities need to store the date of the last data change and the user that changed them.

### Used technologies

- ***Server:***
    - `TypeScript`
    - `PostgreSql`
    - `PrismaOrm`
    - `Express`

- To create the tables in your database using `PrismaORM` enter command:
```
npx prisma migrate dev --name init
```

- For start `server` enter commant:
```
npm run watch

npm run dev
```
