import { Schema, model } from "mongoose";

const CountrySchema = new Schema({
    name: { type: String, unique: true, require: true },
    presidentName: { type: String },
});

const Country = model("Country", CountrySchema);

export async function CCountry(name: string, presidentName: string) {
    await Country.create({ name, presidentName });
}
export async function GCountry() {
    return await Country.find({})
}
export async function PCountry(name: string, presidentName: string, newName: string) {
    await Country.updateMany({ name, presidentName }, { name: newName });
}
export async function DCountry() {
    await Country.deleteMany({});
}

export default Country;