let i = 10;
const i2 = 20;

export default function f1() {
  console.log("f1입니다.");
}

const member = {
  name: "안려환",
  age: 20,
};
const arr1 = [member];
//console.table(arr1);

member.name = "페이커";
//console.log(member);

export { i, i2, member };
