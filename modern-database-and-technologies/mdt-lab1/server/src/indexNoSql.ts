import mongoose from 'mongoose';
require('dotenv').config({ path: __dirname + './../.env' });

import Country, { CCountry, GCountry, PCountry, DCountry } from './mongo-schema/CountrySchema';
import StudiBook, { CStudiBook, GStudiBook, PStudiBook, DStudiBook } from './mongo-schema/StudiBookSchema';
import SpecializationPrice, { CSpecializationPrice, GSpecializationPrice, PSpecializationPrice, DSpecializationPrice } from './mongo-schema/SpecializationPriceSchema';

const uri = process.env.db_url;

const connectDB = async () => {
    try {
        await mongoose.connect(uri as string)
            .then(() => console.log("MongoDB connection."));

        //Country 
        let startCO1 = performance.now();
        for (let i = 0; i < 10; i++) {
            await CCountry(`CountryName${i}`, `PresidentName${i}`);
        }
        let endCO1 = performance.now();
        console.log("Час виконання створення Country: " + (endCO1 - startCO1) + " мс");

        let startCO2 = performance.now();
        const countries = await GCountry();
        let endCO2 = performance.now();
        console.log("Час виконання створення Country: " + (endCO2 - startCO2) + " мс");

        // console.log('All countries:', countries);

        let startCO3 = performance.now();
        for (let i = 0; i < 10; i++) {
            await PCountry(`CountryName${i}`, `PresidentName${i}`, `NewCountryName${i}`);
        }
        let endCO3 = performance.now();
        console.log("Час виконання створення Country: " + (endCO3 - startCO3) + " мс");

        let startCO4 = performance.now();
        await DCountry();
        let endCO4 = performance.now();
        console.log("Час виконання створення Country: " + (endCO4 - startCO4) + " мс");



        // StudiBook
        let startSB1 = performance.now();
        for (let i = 0; i < 10; i++) {
            await CStudiBook(`AuthorFullName${i}`, `BookName${i}`);
        }
        let endSB1 = performance.now();
        console.log("Час виконання створення StudiBook: " + (endSB1 - startSB1) + " мс");

        let startSB2 = performance.now();
        const SubjectBooks = await GStudiBook();
        let endSB2 = performance.now();
        console.log("Час виконання створення StudiBook: " + (endSB2 - startSB2) + " мс");
        // console.log('All books: ', SubjectBooks);

        let startSB3 = performance.now();
        for (let i = 0; i < 10; i++) {
            await PStudiBook(`AuthorFullName${i}`, `BookName${i}`, `NewAuthorFullName${i}`);
        }
        let endSB3 = performance.now();
        console.log("Час виконання створення StudiBook: " + (endSB3 - startSB3) + " мс");

        let startSB4 = performance.now();
        await DStudiBook();
        let endSB4 = performance.now();
        console.log("Час виконання створення StudiBook: " + (endSB4 - startSB4) + " мс");


        // SpecializationPrice
        let startCS1 = performance.now();
        for (let i = 0; i < 10; i++) {
            await CSpecializationPrice(`name${i}`, `description${i}`, i);
        }
        let enCSd1 = performance.now();
        console.log("Час виконання створення спеціалізацій: " + (enCSd1 - startCS1) + " мс");

        let startCS2 = performance.now();
        const specializations = await GSpecializationPrice();
        let enCSd2 = performance.now();
        console.log("Час виконання отримання спеціалізацій: " + (enCSd2 - startCS2) + " мс");

        // console.log('All specializations:', specializations);
        let startCS3 = performance.now();
        for (let i = 0; i < 10; i++) {
            await PSpecializationPrice(`name${i}`, `description${i}`, i, `NewName${i}`);
        }
        let enCSd3 = performance.now();
        console.log("Час виконання оновлення спеціалізацій: " + (enCSd3 - startCS3) + " мс");

        let startCS4 = performance.now();
        await DSpecializationPrice();
        let enCSd4 = performance.now();
        console.log("Час виконання видалення спеціалізацій: " + (enCSd4 - startCS4) + " мс");


        mongoose.connection.close();
    } catch (error) {
        console.error('Error mongoDB: ' + error);
    }
};
connectDB();
export default connectDB;
