import { Schema, model } from 'mongoose';

const SpecializationPriceSchema = new Schema({
    name: { type: String },
    description: { type: String },
    price: { type: Number }
});

const SpecializationPrice = model("SpecializationPrice", SpecializationPriceSchema);

export async function CSpecializationPrice(name: string, description: string, price: Number) {
    await SpecializationPrice.create({ name, description, price });
}
export async function GSpecializationPrice() {
    return await SpecializationPrice.find({})
}
export async function PSpecializationPrice(name: string, description: string, price: Number, newName: string) {
    await SpecializationPrice.updateMany({ name, description, price }, { name: newName });
}
export async function DSpecializationPrice() {
    await SpecializationPrice.deleteMany({});
}

export default SpecializationPrice;