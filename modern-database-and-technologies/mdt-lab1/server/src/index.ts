import * as express from 'express';
import * as cors from 'cors';

require('dotenv').config({ path: __dirname + './../.env' });

import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();

const main = async () => {
    const app = express();
    const PORT = process.env.PORT || 5000;

    app.use(cors());
    app.use(express.json());


    const country1 = await prisma.country.create({
        data: {
            Name: "Ukraine",
            PresidentName: "Volodymyr Zelensky"
        }
    });

    const country2 = await prisma.country.create({
        data: {
            Name: "USA",
            PresidentName: "Joe Biden"
        }
    });

    const user1 = await prisma.user.create({
        data: {
            Email: 'user1@gmail.com',
            Password: 'userpass1',
            FirstName: "user1FN",
            LastName: "user1LN",
            CountryId: country1.Id,
        }
    });

    const user2 = await prisma.user.create({
        data: {
            Email: 'user2@gmail.com',
            Password: 'userpass2',
            FirstName: "user2FN",
            LastName: "user2LN",
            CountryId: country2.Id,
        }
    });

    const about1 = await prisma.aboutUser.create({
        data: {
            UserId: user1.Id,
            FatherName: "FatherName1",
            MotherName: "MotherName1",
            age: 19,
            UpdateAt: new Date(),
            Phone: 12345,
            Telegram: 't.me/user1'
        }
    });

    const about2 = await prisma.aboutUser.create({
        data: {
            UserId: user2.Id,
            FatherName: "FatherName2",
            MotherName: "MotherName2",
            age: 18,
            UpdateAt: new Date(),
            Phone: 54321,
            Telegram: 't.me/user2'
        }
    });

    const userRole1 = await prisma.userRole.create({
        data: {
            UserId: user1.Id,
            Role: 'Starosta',
        }
    });

    const userRole2 = await prisma.userRole.create({
        data: {
            UserId: user2.Id,
            Role: 'Student',
        }
    });


    const subject1 = await prisma.subject.create({
        data: {
            Name: "math",
            score: 60,
        }
    });
    const headTeacher1 = await prisma.headTecher.create({
        data: {
            FirstName: "TeacherFN1",
            LastName: "TEACHERLN1",
            CountryId: country1.Id,
            SubjectId: subject1.Id
        }
    });

    const subject2 = await prisma.subject.create({
        data: {
            Name: "programing",
            score: 70,
        }
    });
    const headTeacher2 = await prisma.headTecher.create({
        data: {
            FirstName: "TeacherFN2",
            LastName: "TEACHERLN2",
            CountryId: country2.Id,
            SubjectId: subject2.Id
        }
    })

    const subjectCollection1 = await prisma.subjectMiddlevare.create({
        data: {
            UserId: user1.Id,
            SubjectId: subject1.Id,
            UserJoinToSubject: new Date(),
            UserExitSubject: new Date()
        }
    });

    const subjectCollection2 = await prisma.subjectMiddlevare.create({
        data: {
            UserId: user2.Id,
            SubjectId: subject2.Id,
            UserJoinToSubject: new Date(),
            UserExitSubject: new Date()
        }
    });

    const teacherAbot1 = await prisma.headTecherAbout.create({
        data: {
            HeadTecherId: headTeacher1.Id,
            Age: 34,
            YearEndUniversity: 2012,
            YearStartWork: 2013,
            UpdateAte: new Date(),
            Phone: 12343,
            Email: "HT1@gmail.com",
            Telegram: "t.me/ht1",
        }
    });

    const teacherAbot2 = await prisma.headTecherAbout.create({
        data: {
            HeadTecherId: headTeacher2.Id,
            Age: 43,
            YearEndUniversity: 2002,
            YearStartWork: 2003,
            UpdateAte: new Date(),
            Phone: 127783,
            Email: "HT2@gmail.com",
            Telegram: "t.me/ht2",
        }
    });

    const teacherRole1 = await prisma.headTecherRole.create({
        data: {
            HeadTecherId: headTeacher1.Id,
            Status: 'Assistant'
        }
    });

    const teacherRole2 = await prisma.headTecherRole.create({
        data: {
            HeadTecherId: headTeacher2.Id,
            Status: 'Docent'
        }
    });

    const university1 = await prisma.university.create({
        data: {
            NameUniv: 'KNU',
            NumberFacultes: 999,
            CountryId: country1.Id
        }
    });

    const university2 = await prisma.university.create({
        data: {
            NameUniv: 'asd',
            NumberFacultes: 19,
            CountryId: country2.Id
        }
    });

    const contractColection1 = await prisma.teacherContractCollection.create({
        data: {
            TeacherId: headTeacher1.Id,
            status: true,
            TeacherJoinToContact: new Date(),
            TeacherExittContact: new Date()
        }
    });

    const contractColection2 = await prisma.teacherContractCollection.create({
        data: {
            TeacherId: headTeacher2.Id,
            status: true,
            TeacherJoinToContact: new Date(),
            TeacherExittContact: new Date()
        }
    });

    const teacherContract1 = await prisma.teacherContract.create({
        data: {
            Salary: 9999,
            Hospital: true,
            ContractYearTerm: 3
        }
    });

    const teacherContrac2 = await prisma.teacherContract.create({
        data: {
            Salary: 333,
            Hospital: false,
            ContractYearTerm: 2
        }
    });

    const faculty1 = await prisma.faculty.create({
        data: {
            Name: "Fcnc",
            DecanId: headTeacher1.Id,
            UniversityId: university1.Id,
            teacherContractId: teacherContract1.Id
        }
    });


    const faculty2 = await prisma.faculty.create({
        data: {
            Name: "asd",
            DecanId: headTeacher2.Id,
            UniversityId: university2.Id,
            teacherContractId: teacherContrac2.Id
        }
    });

    const groupCollection1 = await prisma.groopCollection.create({
        data: {
            Name: "k-26",
            HeadTecherId: headTeacher1.Id,
            FacultyId: faculty1.Id,
            GroupCreateAt: new Date()
        }
    });

    const groupCollection2 = await prisma.groopCollection.create({
        data: {
            Name: "k-21",
            HeadTecherId: headTeacher2.Id,
            FacultyId: faculty2.Id,
            GroupCreateAt: new Date()
        }
    });

    const groupMiddleware1 = await prisma.groupMiddlevare.create({
        data: {
            UserId: user1.Id,
            GroopCollectionId: groupCollection1.Id,
            Status: true,
            UserJoinToGroup: new Date(),
            UserExitGroup: new Date()
        }
    });

    const groupMiddleware2 = await prisma.groupMiddlevare.create({
        data: {
            UserId: user2.Id,
            GroopCollectionId: groupCollection2.Id,
            Status: false,
            UserJoinToGroup: new Date(),
            UserExitGroup: new Date()
        }
    });

    app.listen(PORT, () => {
        console.log(`Server vas satart on port: ${PORT}`)
    });
}

main()
    .catch(e => {
        console.log(e);
    });