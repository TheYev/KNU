import { Schema, model } from "mongoose";

const StudiBookSchema = new Schema({
    AuthorFullName: { type: String },
    BookName: { type: String },
});

const StudiBook = model("StudiBook", StudiBookSchema);

export async function CStudiBook(AuthorFullName: string, BookName: string) {
    await StudiBook.create({ AuthorFullName, BookName });
}
export async function GStudiBook() {
    return await StudiBook.find({})
}
export async function PStudiBook(AuthorFullName: string, BookName: string, newName: string) {
    await StudiBook.updateMany({ AuthorFullName, BookName }, { name: newName });
}
export async function DStudiBook() {
    await StudiBook.deleteMany({});
}

export default StudiBook;