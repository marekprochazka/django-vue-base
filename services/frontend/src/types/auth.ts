// should match definition in services/backend/user/serializers/user.py/BaseUserSerializer
interface IBaseUser {
    pk : number;
    username : string;
    email : string;
    first_name : string;
    last_name : string;
    is_staff : boolean;
    is_superuser : boolean;
}

export type { IBaseUser }